sukupuoli = input('Anna sukupuolesi:')
glarvo = int(input('Anna hemoglobiiniarvosi:'))

if (117>=glarvo or glarvo<=175 and sukupuoli=='nainen'):
    print('Hemoglopiiniarvosi on normaali')
elif (glarvo <117 and sukupuoli== 'nainen'):
    print('Hemoglopiiniarvosi on alheinen')
elif (glarvo >175 and sukupuoli == 'nainen'):
    print('Hemoglopiiniarvosi on korkea')
elif (134>= glarvo or glarvo <=195 and sukupuoli == 'mies'):
    print('Hemoglopiiniarvosi on normaali')
elif (glarvo <134 and sukupuoli == 'mies'):
    print('Hemoglopiiniarvosi on alhainen')
elif (glarvo >195 and sukupuoli == 'mies'):
    print('Hemoglopiiniarvosi on korkea')