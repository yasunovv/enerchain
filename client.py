import web3
import time
abi = [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "AllData",
		"outputs": [
			{
				"internalType": "address",
				"name": "owner",
				"type": "address"
			},
			{
				"internalType": "bytes32",
				"name": "dataCount",
				"type": "bytes32"
			},
			{
				"internalType": "uint256",
				"name": "time",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "fee",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address payable",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "_dataCount",
				"type": "bytes32"
			}
		],
		"name": "sendData",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_fee",
				"type": "uint256"
			}
		],
		"name": "setFee",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]

w3 = web3.Web3(web3.HTTPProvider('https://etc.rivet.link'))
address = "0x4476A57F11DE08725CeB8eAd3f79aAdA1bff9FDe"
mycontract = w3.eth.contract(address=address, abi=abi)
i = 0
while True:
	while True:
		try:
			# Сделать в читаемом виде
			ar = mycontract.functions.AllData(i).call()
			print(ar)
			print('\n')	
			print(ar[0], web3.Web3.toText(ar[1]), ar[2])
			print("<-------------------------------------------------------------------------------------->")	
		except:
			time.sleep(30)
			break
		time.sleep(5)
		i = i + 1


