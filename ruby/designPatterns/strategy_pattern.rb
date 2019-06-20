
# https://www.youtube.com/watch?v=zLgEtOl3eGQ

class Reporter

  def initialize(formatter)
    @formatter = formatter.new
  end

  def report
    stock_left = "template"

    @formatter.format(stock_left)
  end

end

class Formatter1
  def format(data)
    return data + " format1"
  end
end

class Formatter2
  def format(data)
    return data + " format2"
  end
end

r = Reporter.new(Formatter1)
p r.report

s = Reporter.new(Formatter2)
p s.report
