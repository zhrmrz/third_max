class Sol:
    def third_max(self,list):
        fmax=list[0]
        smax=list[0]
        tmax=list[0]
        for i in range(len(list)):
            if list[i]>fmax:
                fmax=list[i]
            elif list[i]>smax:
                smax=list[i]
            elif list[i]>tmax:
                tmax=list[i]
        if len(list)<3:
            return fmax
        return tmax

if __name__ == '__main__':
    p1=Sol()
    print(p1.third_max([1,2]))
