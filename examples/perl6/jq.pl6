#!/usr/bin/env perl6
use JSON::Fast;
say to-json from-json($*IN.slurp), :pretty;
