def pbSelectItemID
  Kernel.pbMessage(_INTL("Script added by https://www.youtube.com/TheCoolKid19"))
  sp = ChooseNumberParams.new
  sp.setRange(1, PBItems.maxValue)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  itemID=Kernel.pbMessageChooseNumber(_INTL("Input the Item ID from the Item ID List"),sp)
  return itemID
end

#Add this Script in PokemonDebug or Debug script
#Use the function in the "additem" function
#Change item=pbListScreen(_INTL("ADD ITEM"),ItemLister.new(0))
#to item=pbSelectItemID