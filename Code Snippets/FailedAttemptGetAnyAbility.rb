def pbChooseAbilityID
  maxNum=PBAbilities.maxValue
  helpText="Input the Ability ID from the file named 'AbilitiesList'"
  Kernel.pbMessage(_INTL("Script added by youtube.com/TheCoolKid19"))
  sp=ChooseNumberParams.new
  sp.setRange(1, maxNum)
  sp.setInitialValue(1)
  sp.setCancelValue(0)
  output=Kernel.pbMessageChooseNumber(_INTL(helpText),sp)
  return output
end

def pbExtractAbilitiesList
  file = File.new("IDs/AbilitiesList.txt", "w")
  maxLength = PBAbilities.maxValue.to_s.length
  for i in 1..PBAbilities.maxValue
    begin
      aname = getConstantName(PBAbilities,i)
    rescue
      aname = "Undefined"
    end
    iLength = i.to_s.length
    zero = "0" * (maxLength - iLength)
    output = zero + i.to_s + " " + aname
    file.puts output
  end
  file.close
  Kernel.pbMessage(_INTL("Ability List Genereted"))
end

pbExtractAbilitiesList