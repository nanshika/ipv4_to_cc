#! /usr/bin/perl
use strict;
use warnings;
use utf8;

###############################################################################
# 元データ                                                                    #
# 適時下記からダウンロードする                                                #
# - ftp://ftp.arin.net/pub/stats/arin/delegated-arin-extended-latest          #
# - ftp://ftp.ripe.net/pub/stats/ripencc/delegated-ripencc-extended-latest    #
# - ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-extended-latest       #
# - ftp://ftp.lacnic.net/pub/stats/lacnic/delegated-lacnic-extended-latest    #
# - ftp://ftp.afrinic.net/pub/stats/afrinic/delegated-afrinic-extended-latest #
###############################################################################
my $RAWDATA  = './ignore/rawdata/*';

if(open(my $fh, "cat $RAWDATA | grep ipv4 | egrep \"allocated|assigned\" |")){
	
	my @ipdata = ();
	my $total  = 0;
	
	# 1 データ読み込み＆10進数化
	while (<$fh>) {
		chomp;
		my (undef, $cc, $type, $start, $value, undef, undef) = split(/\|/);
		my @ipsep = split(/\./, $start);
		my $num = (($ipsep[0] << 24) | ($ipsep[1] << 16) | ($ipsep[2] << 8) | $ipsep[3]);
		
		$ipdata[$total] = ();
		$ipdata[$total][0] = $num;
		$ipdata[$total][1] = $num+$value;
		$ipdata[$total++][2] = $cc;
	}
	close($fh);
	
	# 2 データの集約化
	my $b_cc = "";
	my $b_st = "";
	my $b_en = "";
	my $flg  = 0;
	foreach my $var((sort {$a->[0] <=> $b->[0]} @ipdata)){
		if($var->[2] ne $b_cc || $var->[0] != $b_en){
			if($flg != 0){printf "$b_st,$b_en,$b_cc\n";}
			else{$flg=1;}
			$b_st = $var->[0];
			$b_cc = $var->[2];
		}
		$b_en = $var->[1];
	}
	printf "$b_st,$b_en,$b_cc\n";
}
