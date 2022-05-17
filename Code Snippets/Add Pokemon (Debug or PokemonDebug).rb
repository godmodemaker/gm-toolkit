def selectPokemonID
	Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
	sp = ChooseNumberParams.new
	sp.setRange(1, PBSpecies.maxValue)
	sp.setInitialValue(1)
	sp.setCancelValue(0)
	species=Kernel.pbMessageChooseNumber(_INTL("Input the Pokemon Species ID from the Pokemon ID List"),sp)
	return species
end

species = selectPokemonID

if species!=0
  params=ChooseNumberParams.new
  params.setRange(1,PBExperience::MAXLEVEL)
  params.setInitialValue(5)
  params.setCancelValue(0)
  level=Kernel.pbMessageChooseNumber(_INTL("Set the Pokémon's level."),params)
  if level>0
    pbAddPokemon(species,level)
  end
end