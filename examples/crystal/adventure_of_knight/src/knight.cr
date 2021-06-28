# Have a way to define the location of the treasures
# Regular Knight's tour:
# In the path for each step keep the coordinates and a number indication the location in the 8 possible movies from the previous move.
# The next step is
#    if the length of the path equals to the number of squares then we are done.
#       If we would like to find all the solutions then save this solution and go on
#       else quit
#    the first empty location starting from the last part of the path and trying to go over the 8 possible locations.
#       if none of the 8 are possible and empty then this is a dead-end. Replace the last part with the next location.
#  Given an already existing path the next move is
#     - if we are in the last to add a new square

# recursive:
#  given a path and a list oftreasures to find see if we go over the 8 possible next move, 

class Location
  @x : Int32
  @y : Int32
  getter x
  getter y

  def initialize(x : Int32, y : Int32)
    @x = x
    @y = y
  end

  def initialize(x : Char, y : Int32)
    @x = x.ord - 64
    @y = y
  end

  def to_s
    return "(#{(@x+64).chr}, #{@y})"
  end
end

class Board
  @x : Int32
  @y : Int32
  def initialize(x : Int32, y : Int32)
   @x = x
   @y = y
  end

  def on_board?(location : Location)
    return false if location.x <= 0
    return false if location.y <= 0
    return false if location.x > @x
    return false if location.y > @y
    return true
  end

  def moves(loc : Location)
    possible_moves = [
      Location.new(loc.x + 2, loc.y + 1),
      Location.new(loc.x + 2, loc.y - 1),
      Location.new(loc.x - 2, loc.y + 1),
      Location.new(loc.x - 2, loc.y - 1),
      Location.new(loc.x + 1, loc.y + 2),
      Location.new(loc.x + 1, loc.y - 2),
      Location.new(loc.x - 1, loc.y - 2),
      Location.new(loc.x - 1, loc.y + 2),
    ].reject do |loc| !on_board?(loc) end
  end
end
#a1
#c2
#a3
#c4
#b2
#a4
#c3
#a2
#c1
#
#23444432
#34666643
#46888864
#46888864
#46888864
#46888864
#34666643
#23444432





#treasures = [
#    {"e", 6},
#    {"c", 4},
#]
start_here = {"a", 8}
#p! typeof(start)     # Tuple(String, Int32)
#p! typeof(treasures) # Array(Tuple(String, Int32))


class Knight
  @path = [] of Tuple(String, Int32)
  @current : Tuple(String, Int32)

  def initialize(start)
    @current = start
  end

  def find()
    while (! done?)
      move = next_move
      if move.nil?
        @path.pop
      else
        @path.push(move)
      end
    end
  end

  def next_move
    @current
    return {"b", 3}
  end

  def done?
    return true
  end

  def path
    return @path
  end
end

kn = Knight.new(start_here)
kn.find
puts kn.path

