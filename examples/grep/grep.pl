use strict;
use warnings;

my ($reg, $filename) = @ARGV;
open(my $fh, '<', $filename) or die;
while (my $line = <$fh>) {
   if (index($line, $reg) >= 0) {
       print($line);
   }
}

