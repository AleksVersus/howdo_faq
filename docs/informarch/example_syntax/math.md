# Operation

## math_no_operator

```qsp
y = no 1
if no (x = 1):
	*pl "no — унарный"
end
x = no 2
x = NO 2
x = No 2
x = nO 2
msg "no 2 = <<no 2>>"
msg "NO 2 = <<NO 2>>"
msg "nO 2 = <<nO 2>>"
! `no` без правого операнда — invalid в обоих контекстах (scope avs_wrong_no_with_out_right):
x = NO
msg "<NO> = <<NO>>"
```
