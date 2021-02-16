#ADD COMMA TRYING
import StockStalker.present as pres
import StockStalker.crypto as crypto
import StockStalker.past as past
print(pres.getLiveData("M"))
print(crypto.getCrypto("BTC"))
print(past.getPastData("M", "2/16/2021", "2/10/2021"))






