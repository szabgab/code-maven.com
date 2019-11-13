use strict;
use warnings;
use 5.010;

use File::Find qw(find);

my $dir = shift // '.';

find(\&wanted, $dir);

sub wanted {
    #say $_;
}

