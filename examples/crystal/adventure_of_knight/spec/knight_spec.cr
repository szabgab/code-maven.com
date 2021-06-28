require "spec"
require "../src/knight"

describe "Tools" do
  it "Location" do
    a = Location.new(2, 3)
    a.x.should eq 2
    a.y.should eq 3
    a.to_s.should eq "(B, 3)"

    b = Location.new('A', 4)
    b.x.should eq 1
    b.y.should eq 4
    b.to_s.should eq "(A, 4)"
  end

  it "on_board?" do
    brd = Board.new(8, 8)
    brd.on_board?(Location.new('A', 0)).should be_false
    brd.on_board?(Location.new('A', 1)).should be_true
    brd.on_board?(Location.new('A', 3)).should be_true
    brd.on_board?(Location.new('A', 8)).should be_true
    brd.on_board?(Location.new('A', 9)).should be_false
    brd.on_board?(Location.new('H', 1)).should be_true
    brd.on_board?(Location.new('H', 8)).should be_true
    brd.on_board?(Location.new('I', 1)).should be_false
  end

  it "moves" do
    brd= Board.new(8, 8)
    moves = brd.moves( Location.new('A', 1) ).map &.to_s
    moves.should eq ["(C, 2)", "(B, 3)"]
    #mvs = moves({'A', 3}, {8, 8})
    #mvs.empty?.should be_true
  end
end
