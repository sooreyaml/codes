from solana.rpc.api import Client
from solders.pubkey import Pubkey

client = Client("https://api.mainnet-beta.solana.com")  # Use "https://api.devnet.solana.com" for Devnet
address = Pubkey.from_string("C1u7WJq3hDMDsWwEnYbT8jFi5rDyd1qDiDSeYcwPUXMq")

balance_response = client.get_balance(address)

lamports = balance_response.value  # Directly access `.value`
sol_balance = lamports / 1_000_000_000  # Convert to SOL

print(f"Balance: {sol_balance} SOL")
