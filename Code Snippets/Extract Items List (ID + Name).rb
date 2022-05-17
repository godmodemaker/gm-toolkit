file = File.new("ItemList.txt", "w")
max = PBItems.maxValue
maxl = max.to_s.length
for i in 1..max
  ilen = i.to_s.length
  begin
    iname = getConstantName(PBItems,i)
  rescue
    if iname.eql? ""
      iname = "Unknown"
    end
  end
  zero = "0" * (maxl - ilen)
  output = zero + i.to_s + " " + iname
  file.puts output
end
file.close
Kernel.pbMessage(_INTL("Done"))