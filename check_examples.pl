use strict;
use warnings;
use 5.010;

use File::Find qw(find);
use Path::Tiny qw(path);
use Data::Dumper qw(Dumper);

my %examples;
my %includes;

sub collect_examples {
	return if -d $_;
	#say $_;   # examples/node/argv.js
	$examples{$_} = 1;
}

sub check_articles {
	return if -d $_;
	return if $_ !~ /\.txt$/;
	my $code = path($_)->slurp_utf8;
	$includes{$_}++ for $code =~ m{<(?:try|include) file="([^"]+)">}g;
	#say $_;
}

find({ wanted => \&collect_examples, no_chdir => 1 }, 'examples/');
find({ wanted => \&check_articles, no_chdir => 1 }, 'sites/en/pages');
#print Dumper \%includes;
foreach my $file (keys %examples) {
	if (not delete $includes{$file}) {
		say "File not in use: '$file'";
	}
}
foreach my $file (keys %includes) {
	say "File missing: '$file'";
}

