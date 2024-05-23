
signature IntKey =
struct
    type ord_key = int
    val compare = Int.compare
end

structure seen = BinarySetFn(IntKey)

let 
  val file = TextIO.openIn "input.txt"
  val seen = ref IntMap
  fun loop ins =
      case TextIO.inputLine ins of
           NONE      => []
         | SOME line => 
              case Int.fromString line of 
                   SOME num => num :: loop ins
                 | NONE     => []
  val d = loop file before TextIO.closeIn file
  fun check init, x = 
      let f = init + x in
        seen := seen.add(f);
        x
      end
in
  while 
  foldl (fn(init, x) => x + init) 0 d
end
