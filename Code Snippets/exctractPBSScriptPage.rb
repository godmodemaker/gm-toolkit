def pbExtractPBS
	directory_name = "IDs"
	Dir.mkdir(directory_name) unless File.exists?(directory_name)
	pbExtractSpeciesList
	pbExtractItemList
	pbExtractMoveList
end

def pbExtractSpeciesList
	file = File.new("IDs/PokemonList.txt", "w")
	maxLength = PBSpecies.maxValue.to_s.length
	for i in 1..PBSpecies.maxValue
		begin
			pname = getConstantName(PBSpecies,i)
		rescue
			pname = "Undefined"
		end
	  iLength = i.to_s.length
	  zero = "0" * (maxLength - iLength)
	  output = zero + i.to_s + " " + pname
	  file.puts output
	end
	file.close
	Kernel.pbMessage(_INTL("Species List Genereted"))
end

def pbExtractItemList
	file = File.new("IDs/ItemsList.txt", "w")
	maxLength = PBItems.maxValue.to_s.length
	for i in 1..PBItems.maxValue
		begin
			iname = getConstantName(PBItems,i)
		rescue
			iname = "Undefined"
		end
	  iLength = i.to_s.length
	  zero = "0" * (maxLength - iLength)
	  output = zero + i.to_s + " " + iname
	  file.puts output
	end
	file.close
	Kernel.pbMessage(_INTL("Items List Genereted"))
end

def pbExtractMoveList
	file = File.new("IDs/MoveList.txt", "w")
	maxLength = PBMoves.maxValue.to_s.length
	for i in 1..PBMoves.maxValue
		begin
			mname = getConstantName(PBMoves,i)
		rescue
			mname = "Undefined"
		end
	  iLength = i.to_s.length
	  zero = "0" * (maxLength - iLength)
	  output = zero + i.to_s + " " + mname
	  file.puts output
	end
	file.close
	Kernel.pbMessage(_INTL("Moves List Genereted"))
end