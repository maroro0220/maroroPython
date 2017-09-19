#str_list_ex.py
print( '{0:=^50}'.format( '1' ) )
s = 'hong gil dong20141121623210'

name = s[ :s.rfind( 'g' ) + 1 ]
birthday_index = s.rfind( 'g' ) + 1
birthday = s[ birthday_index: birthday_index + 9 ]
idnumber = s[ s.rfind( 'g' ) + 1: ] 


print( 'Name : ' + name )
print( 'Birthday : ' + birthday[ :4 ] + '/' + birthday[ 4:6 ] + '/' + birthday[ 6:8 ] )
print( 'ID Number : ' + idnumber[ :8 ] + '-' + idnumber[ 8: ] )

print( '{0:=^50}'.format( '2' ) )
s = 'MultiCampus'

print( s[ s.find( 'Campus' ): ] + s[ :s.find( 'Campus' ) ] )

print( '{0:=^50}'.format( '3' ) )

s = 'hello world'

print( 'hi' + ' ' + s[ s.find( 'world' ): ] )

print( '{0:=^50}'.format( '4' ) )
op = [ '+', '-', '*', '/' ]
number1 = input( 'Input number1 : ' )
number2 = input( 'Input number2 : ' )
op_select = int( input( 'Input operator( 1:+, 2:-, 3:*, 4:/ ) : ' ) )

index = op_select - 1
result = eval( number1 + op[ index ] + number2 )

print()
print( 'number1 : {0:^8.2}'.format( number1 ) )
print( 'number2 : {0:^8.2}'.format( number2 ) )
print( '{0:^6} {2:^3} {1:^6} = {3:<.2f}'.format( number1, number2, op[ index ], result ) )

print( '{0:=^50}'.format( '5' ) )
max_number = int( input( 'Input max number : ' ) )

l = list( range( 1, max_number + 1 ) )

print()
print( l )
print( '1 ~ {0:^6} = {1:<8}'.format( max_number, sum( l ) ) )

print( '{0:=^50}'.format( '6' ) )
max_number = int( input( 'Input max number : ' ) )

even = list( range( 2, max_number + 1, 2 ) )
odd = list( range( 1, max_number + 1, 2 ) )

print()
print( 'even number : ', even )
print( '1 ~ {0:^6} = {1:<8}\n'.format( max_number, sum( even ) ) )

print( 'odd number : ', odd )
print( '1 ~ {0:^6} = {1:<8}'.format( max_number, sum( odd ) ) )

print( '{0:=^50}'.format( '7' ) )
max_number = int( input( 'Input max number : ' ) )

l3 = [ x for x in range( 1, max_number + 1 ) if x % 3 == 0 ]
l5 = [ x for x in range( 1, max_number + 1 ) if x % 5 == 0 ]
l = [ x for x in range( 1, max_number + 1 ) if x % 3 != 0 and x % 5 != 0 ]

print()

print( 'Multiple of 3 : ', l3, '\n' )
print( 'Multiple of 5 : ', l5, '\n' )
print( 'Excluding Multiple of 3 and 5 : ', l )
print( 'sum = {0:<6}'.format( sum( l ) ) )
