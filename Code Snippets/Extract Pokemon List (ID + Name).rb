file = File.new("PokemonList.txt", "w")
maxLength = PBSpecies.maxValue.to_s.length
for i in 1..PBSpecies.maxValue
  pname = getConstantName(PBSpecies,i)
  iLength = i.to_s.length
  zero = "0" * (maxLength - iLength)
  output = zero + i.to_s + " " + pname
  file.puts output
end
file.close