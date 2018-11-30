use strict;
use warnings;

# Setting default label
# Set the label $label to $value on each instance (in $project) that does not have that label.

my $project = 'name-of-project';
my $label   = 'stop_at';
my $value   = 'never';

my @lines = qx{gcloud compute instances list --filter="NOT labels.${label}:*" --format='csv[no-heading](zone,name)' --project $project};
for my $line (@lines) {
   chomp $line;
   my ($zone, $name) = split /,/, $line;
   #print "$zone\n   $name\n";
   my $cmd = qq{gcloud compute instances add-labels $name --labels="${label}=${value}" --zone $zone --project $project};
   #print "$cmd\n";
   system $cmd;
}
