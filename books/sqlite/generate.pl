use strict;
use warnings;

sub big_data {
    my $n = 100_000;
    my $text = "name,value\n";
    my $name = "aaaaaaaa";
    for my $i (1..$n) {
        $text .= "$name,$i\n";
        $name++;
    }
    open my $fh, ">", "examples/big-data.csv" or die;
    print $fh $text;
    close $fh;
}

big_data();


