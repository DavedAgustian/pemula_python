class Lain:
    def jam(self):
        print('tanggal sekarang jam')
    def menit(self):
        print ('tanggal sekarang menit')

    def __call__(self):
        print('tanggal sekarang')
class Tanggal:

    def __init__(self):
        self.sekarang=Lain()
    def __call__(self,word):
        print(word)




tanggal = Tanggal()
tanggal.sekarang()
tanggal.sekarang.jam()
tanggal('hello')
tanggal('besok')
tanggal.sekarang.menit()
