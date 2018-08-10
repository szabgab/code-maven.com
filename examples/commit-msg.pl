#!/usr/bin/perl
use strict;
use warnings;
use autodie;

my @tasks  = qw(refactoring design bug);

my $filename = shift;
open my $fh, '<', $filename;
my $line = <$fh>;
my ($task) = $line =~ /^#(\w+) - /;
my $error;

if ($task) {
    if (grep { $task eq $_ } @tasks) {
        # OK
    } else {
        $error = "Invalid task '$task'.";
    }
} else {
    $error = 'Invalid message format.'; 
}

if ($error) {
    die "****** $error\nThe message needs to start with '#TASK - ' where TASK is one of the following:\n@tasks\n";
}

