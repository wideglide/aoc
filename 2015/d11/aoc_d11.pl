

my $start = 'vzbxkghb';
my $flag = 1;

while(++$start) {
  if ($start =~ /(\w)\1.*(\w)\2/g) {
    if ($start !~ /[ilo]/g) {
      if ($start =~ /(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)/) {
        print "$start : \n";
        break;
      }
    }
  }
}
