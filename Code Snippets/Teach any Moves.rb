  def pbChooseMoveNum
    sp = ChooseNumberParams.new
    sp.setRange(1, PBSpecies.maxValue)
    sp.setInitialValue(1)
    sp.setCancelValue(0)
    species=Kernel.pbMessageChooseNumber(_INTL("Input the Move number from the Move List"),sp)
    return species
  end

  #Just add this function in PokemonParty under the class PokemonScreen
  #And then in the Moves Option of Debug, set the variable 'move' as below:
  #move=pbChooseMoveNum