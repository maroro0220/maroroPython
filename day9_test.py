from collections import namedtuple


print('Prob. #6'.center(60,'='),'\n')
class View:
      menu='''
1. 품목 정보 등록
2. 판매 정보 등록
3. 판매 현황표 출력
0. 종료
        '''

      def __init__(self):
            self.prodinfo=ProdInfo()
            self.soldinfo=SoldInfo()
            self.soldprint=SoldPrint()
            self.menuC={1:self.prodinfo,2:self.soldinfo,3:self.soldprint}
            self.prodinfo.prodinfolist=[]
            self.soldinfo.soldinfolist=[]
            self.soldprint.soldprintlist=[]
            
      
      def selectmenu(self):
            print(self.menu)
            self.selm=int(input('select menu'))
            while self.selm!=0:
                  
                  if self.selm==1 or self.selm==2:
                        self.menuC[self.selm].iinput()
                  else:
                        self.menuC[self.selm].sprint()
                  self.selm=int(input('select menu'))
            
class ProdInfo:
      def __init__(self):
            self.PInfo= namedtuple('ProdInfo','name, price')
            
            
      def iinput(self):

            print('품목 정보 등록')
            self.pname=input('product name')
            self.price=input('price')
            self.produ=self.PInfo(self.pname,self.price)
            self.prodinfolist.append(self.produ)
            print(self.prodinfolist)
            with open('C:\maroroWorkspace\\day9info.txt','a') as self.f:
                  self.pl=len(self.prodinfolist)
                  self.f.writelines(self.prodinfolist[self.pl-1][0]+' '+self.prodinfolist[self.pl-1][1]+'\n')
                  


class SoldInfo:
      def __init__(self):
            self.SInfo= namedtuple('SoldInfo','name, num')
        # 품목명, 판매 수량
            
      def iinput(self):
            print('판매 정보 등록')
            self.pname=input('prod name')
            self.snum=input('number of sold this prod')
            self.produ=self.SInfo(self.pname,self.snum)
            self.soldinfolist.append(self.produ)
            print(self.soldinfolist)
            with open('C:\maroroWorkspace\\day9info.txt','a') as self.f:
                  self.sl=len(self.soldinfolist)
                  self.f.writelines('sold info:'+self.soldinfolist[self.sl-1][0]+' number of sold:'+self.soldinfolist[self.sl-1][1]+'\n')
class SoldPrint():
      def __init__(self):
            self.pi=ProdInfo()
            self.si=SoldInfo()
            
        #품목명, 단가, 판매수량, 판매 금액
      def sprint(self):
            print('판매 현황 출력')
            for self.x in self.pi.prodinfolist:
                  for self.y in self.si.soldinfolist:
                        if self.x.name==self.y.name:
                              self.tot=self.x.price*self.y.num
                              print('name: {0:<5} price: {1:3} num: {2:3} tot: {3:3}'.format(self.x.name, self.x.price, self.y.num, self.tot))
                              with open('C:\maroroWorkspace\\day9soldprint.txt','a') as self.f:
                                    self.f.writelines('name: {0:<5} price: {1:3} num: {2:3} tot: {3:3}'.format(self.x.name, self.x.price, self.y.num, self.tot))

if __name__ == '__main__':
    view = View()
    view.selectmenu()
