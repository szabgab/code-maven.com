use strict;
use warnings;

use Test::More;
use Future::AsyncAwait;
use IO::Async::Loop;
use Net::Async::Redis::XS;

my $key = 'some-key';
my $value = 'some-value';

my $host = $ENV{REDIS_HOST};

plan skip_all => 'Set REDIS_HOST to run this test' if not $host;

my $loop = IO::Async::Loop->new;
$loop->add(my $redis = Net::Async::Redis::XS->new);
$redis->configure(host => $host);
await $redis->connect;
await $redis->set($key, $value);
my $result = await $redis->get($key);
is $result, $value;

done_testing();

