# Tests for Record — validates behavior preservation after composition refactoring.
#
# Run with: ruby tests/test_record.rb

require 'minitest/autorun'
require_relative '../before/record'

class RecordTest < Minitest::Test
  def test_save_output_order
    # The original mixin-based save produces:
    # [Validatable] Saving...
    # [Loggable] Saving...
    # [Record] Saving to database

    record = Record.new
    # Capture stdout to verify output
    output = capture_io { record.save }.first
    lines = output.split("\n")

    assert_match /Validatable/, lines[0], "First should be validation"
    assert_match /Loggable/, lines[1], "Second should be logging"
    assert_match /Record/, lines[2], "Third should be database save"
  end

  def test_save_returns_something
    record = Record.new
    result = record.save
    # save returns nil in the original — just verify it doesn't crash
    assert_nil result
  end
end
