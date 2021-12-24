import math

def determine_packet(binary_value, pos):
	print(binary_value[pos:])
	packet_version = int(binary_value[pos:pos+3],2)
	print("version num: " + str(packet_version))
	packet_type = int(binary_value[pos+3:pos+6],2)
	# print(packet_type)
	if packet_type == 4:
		result = literal_val(binary_value, pos+6)
		print(result)
		return result
	else:
		result, pos = operator_val(binary_value, pos+6)
		print(result)
		if packet_type == 0:
			return sum(result), pos
		elif packet_type == 1:
			return math.prod(result), pos
		elif packet_type == 2:
			return min(result), pos
		elif packet_type == 3:
			return max(result), pos
		elif packet_type == 5:
			if result[0] > result[1]:
				return 1, pos
			else:
				return 0, pos
		elif packet_type == 6:
			if result[0] < result[1]:
				return 1, pos
			else:
				return 0, pos
		elif packet_type == 7:
			if result[0] == result[1]:
				return 1, pos
			else:
				return 0, pos


def literal_val(binary_value, pos):
	print("literal")
	length = 0
	values = []
	# literal_values = binary_value[pos:]
	while binary_value[pos] != "0":
		values.append(binary_value[pos+1:pos+5])
		pos += 5
		length += 5
	else:
		values.append(binary_value[pos+1:pos+5])
		pos += 5
		length += 5
		# value = int(''.join(values),2)
	return int(''.join(values),2), pos

def operator_val(binary_value, pos):
	print("operator")
	length_type_id = binary_value[pos]
	# operator_values = binary_value[pos+7:]
	values = []

	if length_type_id == '0':
		total_length = int(binary_value[pos+1:pos+16],2)
		# print("total length" + str(total_length))
		pos += 16
		current_length = 0
		while current_length < total_length:
			value, position = determine_packet(binary_value, pos)
			values.append(value)
			current_length += position-pos
			pos = position

	elif length_type_id == '1':
		total_number = int(binary_value[pos+1:pos+12],2)
		# print("Total Number" + str(total_number))
		pos += 12
		for i in range(total_number):
			value, position = determine_packet(binary_value, pos)
			values.append(value)
			pos = position
		# print(subpackets)
	return values, pos


# line = "C200B40A82"
# line = "04005AC33890"
# line = "880086C3E88112"
# line = "CE00C43D881120"
# line = "D8005AC2A8F0"
# line = "F600BC2D8F"
# line = "9C005AC2F8F0"
# line = "9C0141080250320F1802104A08"

with open("day16_input") as f:
	line = f.read().strip()

	binary_value = ""
	for char in line:
		binary_value += str(bin(int(char,16)))[2:].zfill(4)

	print(determine_packet(binary_value, 0))
# print(versions, sum(versions))