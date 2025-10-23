<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code># 💬 Bitcoin Message Transaction Creator<br><br>[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)<br>[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)<br>[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)<br>[![Bitcoin](https://img.shields.io/badge/Bitcoin-OP__RETURN-orange.svg)](https://en.bitcoin.it/wiki/OP_RETURN)<br><br>Create Bitcoin transactions with embedded OP_RETURN messages. This tool allows you to permanently store text messages on the Bitcoin blockchain while sending BTC to any address.<br><br>## 🌟 Features<br><br>- ✅ **OP_RETURN Message Embedding** - Store up to 80 bytes of data on-chain<br>- ✅ **Interactive UI** - User-friendly interface in Google Colab<br>- ✅ **CLI Version** - Command-line interface for desktop use<br>- ✅ **Automatic Change Calculation** - Returns remaining funds to sender<br>- ✅ **Testnet &amp; Mainnet Support** - Test safely before going live<br>- ✅ **Transaction Export** - Save RawTX to file for broadcasting<br>- ✅ **Real-time Message Length Validation** - Prevents errors before creation<br><br>## 📋 Table of Contents<br><br>- [Installation](#-installation)<br>- [Usage](#-usage)<br>  - [Google Colab Version](#-google-colab-version)<br>  - [Python CLI Version](#-python-cli-version)<br>- [Broadcasting Transaction](#-broadcasting-transaction)<br>- [Requirements](#-requirements)<br>- [Examples](#-examples)<br>- [Security](#-security)<br>- [Contributing](#-contributing)<br>- [License](#-license)<br><br>---<br><br>## 🚀 Installation<br><br>### Prerequisites<br><br>- Python 3.6 or higher<br>- Git<br><br>### Clone Repository<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>git clone <a rel="noreferrer noopener" target="_blank" href="https://github.com/zoeir/Bitcoin-Message-Transaction.git">https://github.com/zoeir/Bitcoin-Message-Transaction.git</a><br>cd Bitcoin-Message-Transaction</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>### Install Dependencies<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>pip install pycryptodome</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>---<br><br>## 📖 Usage<br><br>### 🌐 Google Colab Version<br><br>Perfect for users who want a graphical interface without installing anything locally.<br><br>#### Step 1: Open Google Colab<br><br>Navigate to [Google Colab](https://colab.research.google.com/)<br><br>#### Step 2: Create New Notebook<br><br>Click **File** → **New Notebook**<br><br>#### Step 3: Install Dependencies<br><br>Copy and paste this code into the first cell:<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>!pip install ipywidgets zmq urllib3 requests pycryptodome<br>!git clone <a rel="noreferrer noopener" target="_blank" href="https://github.com/zoeir/Bitcoin-Message-Transaction.git">https://github.com/zoeir/Bitcoin-Message-Transaction.git</a> &gt; /dev/null 2&gt;&amp;1<br>%cd Bitcoin-Message-Transaction</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>Run the cell (press `Shift + Enter`)<br><br>#### Step 4: Load the Script<br><br>In a new cell, copy the entire content of [`colab.py`](colab.py) and run it.<br><br>#### Step 5: Fill the Form<br><br>An interactive form will appear with the following fields:<br><br>| Field | Description | Example |<br>|-------|-------------|---------|<br>| 🔑 **Private Key (WIF)** | Your Bitcoin private key in WIF format | `5J64pq77XjeacCezwmAr2V1s7snvvJkuAz8sENxw7xCkikceV6e` |<br>| 🆔 **UTXO TXID** | Transaction ID containing your funds | `2a29fdb4e188f827da3c3175856b3ed95819b323bb303a46b8036534e78c76db` |<br>| 🔢 **UTXO Index** | Output index (usually 0) | `0` |<br>| 💰 **UTXO Value** | Amount in satoshi | `30352330` |<br>| 💸 **Transaction Fee** | Network fee (500-10000 sat) | `1000` |<br>| 📤 **Send Amount** | Amount to send in satoshi | `600` |<br>| 📍 **Recipient Address** | Destination Bitcoin address | `1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC` |<br>| 💬 **Message** | Your text message (max 80 bytes) | `Hello Bitcoin!` |<br>| 🧪 **Use Testnet** | Enable for testing | ☑️ Checked |<br><br>#### Step 6: Create Transaction<br><br>Click **"Create Bitcoin Transaction"** button<br><br>#### Step 7: Copy RawTX<br><br>The output will display:<br>- ✅ Your BTC Address<br>- ✅ Recipient Address  <br>- ✅ Send Amount<br>- ✅ Transaction Fee<br>- ✅ Change Returned<br>- ✅ OP_RETURN Message<br>- ✅ **RawTX (Hex)** ← Copy this for broadcasting<br><br>---<br><br>### 🖥️ Python CLI Version<br><br>For users who prefer command-line interface on their desktop/laptop.<br><br>#### Step 1: Navigate to Repository<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>cd Bitcoin-Message-Transaction</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>#### Step 2: Run the Script<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>python3 main.py</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>#### Step 3: Follow Interactive Prompts<br><br>The script will ask for:<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">============================================================<br>BITCOIN MESSAGE TRANSACTION CREATOR</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Enter your Private Key (WIF): 5J64pq77Xjeac...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>--- UTXO Information ---<br>Enter UTXO TXID: 2a29fdb4e188f827...<br>Enter UTXO Index (default 0): 0<br>Enter UTXO Value (satoshi): 30352330</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>--- Transaction Details ---<br>Enter Recipient Address: 1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC<br>Enter Send Amount (satoshi): 600<br>Enter Transaction Fee (satoshi, default 1000): 1000</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>--- OP_RETURN Message ---<br>Enter your message (up to 80 bytes): Hello Bitcoin!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>--- Network Selection ---<br>Use Testnet? (y/n, default y): y</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>#### Step 4: Review Output<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:heading {"level":1} -->
<h1 class="wp-block-heading">============================================================<br>BITCOIN TRANSACTION (OP_RETURN)</h1>
<!-- /wp:heading -->

<!-- wp:paragraph -->
<p>Your BTC Address: 14NWDXkQwcGN1Pd9fboL8npVynD5SfyJAE<br>Recipient Address: 1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC<br>Send Amount: 600 satoshi<br>Transaction Fee: 1000 satoshi<br>Change Returned: 30350730 satoshi</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>OP_RETURN Message: Hello Bitcoin!</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>RawTX (Hex):<br>0100000001db768ce7346503b8463a30bb23b31958d93e6b8575313cda...</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>============================================================<br>✓ Transaction saved to file: RawTX_OP_RETURN.txt</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>---<br><br>## 📡 Broadcasting Transaction<br><br>After creating your transaction, broadcast it using any of these services:<br><br>### Mainnet Services<br><br>| Service | URL |<br>|---------|-----|<br>| 🌐 **Bitcoin Message** | [bitcoinmessage.ru](https://bitcoinmessage.ru) |<br><br><br><br><br><br><br>**Steps:**<br>1. Copy your **RawTX (Hex)** from the output<br>2. Visit any broadcast service above<br>3. Paste the RawTX into the form<br>4. Click "Broadcast" or "Push"<br>5. Wait for confirmation ⏱️<br><br>---<br><br>## 📦 Requirements<br><br>### Python Packages<br><br>- `pycryptodome` - Cryptographic library<br>- `ipywidgets` (Colab only) - Interactive widgets<br>- `IPython` (Colab only) - Display utilities<br><br>### Repository Dependencies<br><br>This tool requires modules from [Bitcoin-Message-Transaction](https://github.com/zoeir/Bitcoin-Message-Transaction):<br>- `secp256k1.py` - Elliptic curve operations<br>- `sighash.py` - Transaction signing<br><br>---<br><br>## 💡 Examples<br><br>### Example 1: Simple Message<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Message: "Hello from the blockchain!"<br>Send Amount: 1000 satoshi<br>Fee: 1000 satoshi</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>### Example 2: Timestamp Proof<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Message: "Document hash: 5d41402abc4b2a76b9719d911017c592"<br>Send Amount: 546 satoshi (dust limit)<br>Fee: 2000 satoshi</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>### Example 3: Identity Proof<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>Message: "github.com/yourname - Verified 2025-10-23"<br>Send Amount: 600 satoshi<br>Fee: 1500 satoshi</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>---<br><br>## 🔒 Security<br><br>### ⚠️ Important Security Notes<br><br>- **Never share your private key** with anyone<br>- **Test on Testnet first** before using real BTC<br>- **Double-check addresses** before broadcasting<br>- **Backup your private keys** securely offline<br>- **Use secure connections** when broadcasting transactions<br>- **OP_RETURN data is permanent** and cannot be deleted<br><br>### Best Practices<br><br>1. ✅ Use testnet for testing<br>2. ✅ Verify recipient address multiple times<br>3. ✅ Start with small amounts<br>4. ✅ Keep private keys in encrypted storage<br>5. ✅ Never commit private keys to Git<br><br>---<br><br>## 🤝 Contributing<br><br>Contributions are welcome! Please feel free to submit a Pull Request.<br><br>### Development Setup<br><br></code></pre>
<!-- /wp:preformatted -->

<!-- wp:paragraph -->
<p>git clone <a rel="noreferrer noopener" target="_blank" href="https://github.com/zoeir/Bitcoin-Message-Transaction.git">https://github.com/zoeir/Bitcoin-Message-Transaction.git</a><br>cd Bitcoin-Message-Transaction<br>pip install -r requirements.txt</p>
<!-- /wp:paragraph -->

<!-- wp:preformatted -->
<pre class="wp-block-preformatted"><code><br>### Reporting Issues<br><br>Please use the [GitHub Issues](https://github.com/zoeir/Bitcoin-Message-Transaction/issues) page to report bugs or request features.<br><br>---<br><br>## 📄 License<br><br>This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.<br><br>---<br><br>## 🙏 Acknowledgments<br><br>- Bitcoin Core developers<br>- [Bitcoin-Message-Transaction](https://github.com/zoeir/Bitcoin-Message-Transaction) repository<br>- Python cryptography community<br><br>---<br><br>## 📞 Support<br><br>- 🌐 Website: [bitcoinmessage.ru](https://bitcoinmessage.ru)<br>- 📧 Issues: [GitHub Issues](https://github.com/zoeir/Bitcoin-Message-Transaction/issues)<br>- 💬 Discussions: [GitHub Discussions](https://github.com/zoeir/Bitcoin-Message-Transaction/discussions)<br><br>---<br><br>## ⭐ Star History<br><br>If you find this project useful, please consider giving it a star! ⭐<br><br>---<br><br>**Made with ❤️ for the Bitcoin community**<br><br>---<br><br>## 📸 Screenshots<br><br>### Google Colab Interface<br>![Colab Interface](https://via.placeholder.com/800x400?text=Google+Colab+Interface)<br><br>### CLI Version Output<br>![CLI Output](https://via.placeholder.com/800x400?text=CLI+Version+Output)<br><br>---<br><br>## 🔗 Related Projects<br><br>- [Bitcoin Core](https://github.com/bitcoin/bitcoin)<br>- [Electrum](https://github.com/spesmilo/electrum)<br>- [BTCPay Server](https://github.com/btcpayserver/btcpayserver)<br><br>---<br><br>## 📊 Statistics<br><br>![GitHub stars](https://img.shields.io/github/stars/zoeir/Bitcoin-Message-Transaction?style=social)<br>![GitHub forks](https://img.shields.io/github/forks/zoeir/Bitcoin-Message-Transaction?style=social)<br>![GitHub issues](https://img.shields.io/github/issues/zoeir/Bitcoin-Message-Transaction)<br>![GitHub pull requests](https://img.shields.io/github/issues-pr/zoeir/Bitcoin-Message-Transaction)<br><br>---<br><br>**Happy Coding! 🚀**<br></code></pre>
<!-- /wp:preformatted -->

