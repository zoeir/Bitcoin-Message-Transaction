# ===================================================
#  Bitcoin Message Transaction (Google Colab Version)
# ===================================================

# Install dependencies (run once if needed)
# !pip install ipywidgets zmq urllib3 requests pycryptodome

# Clone source code repository if not yet downloaded
# !git clone https://github.com/zoeir/Bitcoin-Message-Transaction.git > /dev/null 2>&1
# %cd Bitcoin-Message-Transaction

# Import required modules
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from secp256k1 import *
from sighash import *

# ---------- Functions ----------
def create_op_return_script(message):
    message_hex = message.encode('utf-8').hex()
    message_bytes = bytes.fromhex(message_hex)
    op_return_opcode = b'\x6a'

    data_length = len(message_bytes)
    if data_length <= 75:
        length_byte = bytes([data_length])
    elif data_length <= 255:
        length_byte = b'\x4c' + bytes([data_length])
    else:
        raise ValueError("Message is too long. Maximum allowed is 80 bytes for OP_RETURN.")

    return op_return_opcode + length_byte + message_bytes


def create_transaction_with_op_return(private_key_wif, utxo_txid, utxo_index,
                                      utxo_value, recipient_address,
                                      send_amount, message, fee=1000,
                                      testnet=True):
    pk = PrivateKey.parse(private_key_wif)

    tx_in = TxIn(bytes.fromhex(utxo_txid), utxo_index, b'', 0xffffffff)
    tx_in._script_pubkey = Tx.get_address_data(pk.address())['script_pubkey']
    tx_in._value = utxo_value
    tx_ins = [tx_in]

    # Calculate change (returned to sender)
    change_amount = utxo_value - send_amount - fee
    if change_amount < 0:
        raise ValueError("Insufficient funds to cover the amount and transaction fee.")

    # Transaction outputs
    tx_outs = []
    tx_outs.append(TxOut(0, create_op_return_script(message)))
    tx_outs.append(TxOut(send_amount, Tx.get_address_data(recipient_address)['script_pubkey'].serialize()))
    if change_amount > 546:  # dust limit
        tx_outs.append(TxOut(change_amount, Tx.get_address_data(pk.address())['script_pubkey'].serialize()))

    tx = Tx(1, tx_ins, tx_outs, 0, testnet=testnet)
    signature(tx, 0, pk)

    # Return both transaction and change amount
    return tx, change_amount


# ---------- User Interface ----------
private_key_wif = widgets.Text(placeholder='Enter your private key (WIF)', description='Private Key (WIF):', layout=widgets.Layout(width='75%'))
utxo_txid = widgets.Text(placeholder='Enter UTXO TXID', description='UTXO TXID:', layout=widgets.Layout(width='75%'))
utxo_index = widgets.BoundedIntText(value=0, min=0, max=100, description='UTXO Index:')
utxo_value = widgets.IntText(value=0, description='UTXO Value (satoshi):')
fee = widgets.IntSlider(value=1000, min=500, max=10000, step=100, description='Transaction Fee (sat):')
send_amount = widgets.IntText(value=0, description='Send Amount (sat):')
recipient_address = widgets.Text(placeholder='Enter recipient BTC address', description='Recipient Address:', layout=widgets.Layout(width='75%'))
message = widgets.Textarea(placeholder='Enter your OP_RETURN message (up to 80 bytes)', description='Message:', layout=widgets.Layout(width='90%', height='80px'))
byte_warning = widgets.HTML(value="<span style='color:gray'>0 / 80 bytes</span>")
use_testnet = widgets.Checkbox(value=True, description='Use Testnet')
submit_button = widgets.Button(description='Create Bitcoin Transaction', button_style='success', layout=widgets.Layout(width='40%'))

def update_message_length(change):
    current_bytes = len(change['new'].encode('utf-8'))
    if current_bytes > 80:
        byte_warning.value = f"<span style='color:red; font-weight:bold;'>Message too long: {current_bytes} / 80 bytes!</span>"
    else:
        byte_warning.value = f"<span style='color:green'>{current_bytes} / 80 bytes</span>"

message.observe(update_message_length, 'value')

form = widgets.VBox([
    private_key_wif, utxo_txid, utxo_index, utxo_value, fee,
    send_amount, recipient_address, message, byte_warning,
    use_testnet, submit_button
])
display(form)

# ---------- Processing ----------
def on_submit_clicked(b):
    clear_output(wait=True)
    display(form)
    try:
        tx, change_amount = create_transaction_with_op_return(
            private_key_wif=private_key_wif.value,
            utxo_txid=utxo_txid.value,
            utxo_index=utxo_index.value,
            utxo_value=int(utxo_value.value),
            recipient_address=recipient_address.value,
            send_amount=int(send_amount.value),
            message=message.value,
            fee=int(fee.value),
            testnet=use_testnet.value
        )
        raw_tx_hex = tx.serialize().hex()
        pk = PrivateKey.parse(private_key_wif.value)

        # ---------- Display information ----------
        print("\n===============================")
        print(" BITCOIN TRANSACTION (OP_RETURN)")
        print("===============================")
        print(f"Your BTC Address:         {pk.address()}")
        print(f"Recipient Address:        {recipient_address.value}")
        print(f"Send Amount:              {send_amount.value} satoshi")
        print(f"Transaction Fee:          {fee.value} satoshi")
        print(f"Change Returned:          {change_amount} satoshi")
        print(f"\nOP_RETURN Message:        {message.value}")
        print(f"\nRawTX (Hex):\n{raw_tx_hex}\n")

        with open("RawTX_OP_RETURN.txt", 'w') as f:
            f.write(raw_tx_hex + "\n")
            f.write(f"\nMessage: {message.value}\n")
            f.write(f"Hex: {message.value.encode('utf-8').hex()}\n")
            f.write(f"Change Returned: {change_amount} satoshi\n")

        print("✓ Saved to file: RawTX_OP_RETURN.txt\n")
        print("You can broadcast the transaction using:\nhttps://bitcoinmessage.ru\n")

    except Exception as e:
        print(f"Error: {e}")

submit_button.on_click(on_submit_clicked)
