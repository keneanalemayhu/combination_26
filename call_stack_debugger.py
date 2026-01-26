class StackFrame:
    def __init__(self, function_name, return_address=None, caller=None):
        self.function_name = function_name
        self.locals = {}
        self.return_address = return_address
        self.caller = caller


class CallStackDebugger:
    def __init__(self):
        self.stack = []
        self.max_depth = None

    # SET MAX STACK DEPTH
    def set_max_depth(self, d):
        self.max_depth = d
        print(f"Max stack depth set to {d}.")

    # CALL FUNCTION
    def call(self, function_name):
        if self.max_depth is not None and len(self.stack) >= self.max_depth:
            print(f"Error: Stack Overflow! Max depth ({self.max_depth}) exceeded.")
            return

        caller = self.stack[-1] if self.stack else None
        frame = StackFrame(function_name, caller=caller)
        self.stack.append(frame)

        print(f"Entered: {function_name}. Depth: {len(self.stack)}.")

    # RETURN FROM FUNCTION
    def ret(self):
        if not self.stack:
            print("Error: Call stack is empty.")
            return

        finished = self.stack.pop()
        current = self.stack[-1].function_name if self.stack else "None"
        print(f"Returned from {finished.function_name}. Depth: {len(self.stack)}. Current: {current}.")

    # SET VARIABLE
    def set_var(self, var, value):
        if not self.stack:
            print("Error: No active function.")
            return

        self.stack[-1].locals[var] = value
        print(f"{var} = {value} in {self.stack[-1].function_name}.")

    # GET VARIABLE (SCOPE CHAIN)
    def get_var(self, var):
        frame = self.stack[-1] if self.stack else None

        while frame:
            if var in frame.locals:
                print(f"{var} = {frame.locals[var]} (found in frame: {frame.function_name}).")
                return
            frame = frame.caller

        print(f"Error: Variable '{var}' not found in scope chain.")

    # PRINT STACK TRACE
    def trace(self):
        if not self.stack:
            print("Stack is empty.")
            return

        print("Stack Trace:")
        for i in range(len(self.stack) - 1, -1, -1):
            frame = self.stack[i]
            marker = " (current)" if i == len(self.stack) - 1 else ""
            print(f"  [{i + 1}] {frame.function_name}{marker}")
            for var, val in frame.locals.items():
                print(f"      {var} = {val}")


def main():
    debugger = CallStackDebugger()

    while True:
        try:
            command = input("> ").strip().split()
            if not command:
                continue

            if command[0] == "SET_MAX_DEPTH":
                debugger.set_max_depth(int(command[1]))

            elif command[0] == "CALL":
                debugger.call(command[1])

            elif command[0] == "RETURN":
                debugger.ret()

            elif command[0] == "SET":
                debugger.set_var(command[1], command[2])

            elif command[0] == "GET":
                debugger.get_var(command[1])

            elif command[0] == "TRACE":
                debugger.trace()

            elif command[0] == "EXIT":
                break

            else:
                print("Unknown command.")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()
