file = File.new("ItemList.txt", "w")
for i in 1..PBItems.maxValue
  cname=getConstantName(PBItems,i)
  file.puts cname
end
file.close