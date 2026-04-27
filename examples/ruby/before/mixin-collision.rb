# Before: Mixin collision — two modules define the same method,
# causing silent override and confusing behavior.

module Loggable
  def save
    puts "[Loggable] Saving..."
    super
  end
end

module Validatable
  def save
    puts "[Validatable] Validating..."
    super
  end
end

class Record
  include Loggable
  include Validatable

  def save
    puts "[Record] Saving to database"
  end
end

record = Record.new
record.save
# Output:
# [Validatable] Saving...
# [Loggable] Saving...
# [Record] Saving to database
# Wait — Validatable runs before Loggable? The order depends on include order.
# If someone changes the include order, behavior changes silently.
