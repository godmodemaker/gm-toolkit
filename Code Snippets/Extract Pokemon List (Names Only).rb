file = File.new("PokemonList.txt", "w")
for i in 1..PBSpecies.maxValue
  pname = getConstantName(PBSpecies,i)
  file.puts pname
end
file.close