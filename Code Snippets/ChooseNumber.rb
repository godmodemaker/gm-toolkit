# def pbChooseNumber(input)
#   if input==0
#     maxNum=PBSpecies.maxValue
#     helpText="Input the Pokemon ID from the file named 'PokemonList'"
#   elsif input==1
#     maxNum=PBItems.maxValue
#     helpText="Input the Item ID from the file named 'ItemList'"
#   elsif input==2
#     maxNum=PBMoves.maxValue
#     helpText="Input the Move ID from the file named 'MoveList'"
#   else
#     maxNum=0
#   end
#   Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
#   sp=ChooseNumberParams.new
#   sp.setRange(1, maxNum)
#   sp.setInitialValue(1)
#   sp.setCancelValue(0)
#   output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
#   return output
# end

def pbChoosePokemonID
  maxNum=PBSpecies.maxValue
  helpText="Input the Pokemon ID from the file named 'PokemonList'"
  Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end
  
def pbChooseItemID
  maxNum=PBItems.maxValue
  helpText="Input the Item ID from the file named 'ItemList'"
  Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end

def pbChooseMoveID
  maxNum=PBMoves.maxValue
  helpText="Input the Move ID from the file named 'MoveList'"
  Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end