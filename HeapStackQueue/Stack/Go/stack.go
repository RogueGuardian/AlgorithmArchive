type Stack struct {
    stack []interface{}
}

func (S *Stack) Push(item interface{}) {
    S.stack = append(S.stack, item)
}

func (S *Stack) Pop() interface{} {
    item := S.stack[len(S.stack)-1]
    S.stack[len(S.stack)-1] = nil
    S.stack = S.stack[:len(S.stack)-1]
    return item
}

func (S *Stack) GetSize() int {
    return len(S.stack)
}
