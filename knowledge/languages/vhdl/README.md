# VHDL / Verilog Architecture Idioms

## Use When

- Reviewing HDL code for FPGA or ASIC design, finite state machines, data path architecture, or testbench structure.

## Heuristics

- Separate combinational and sequential logic into distinct processes/always blocks.
- Use enumerated types for FSM states — avoid magic constants.
- Keep reset logic simple — use synchronous reset unless async is required.
- Use generics/parameters for configurable module width and depth.
- Use pipelining to break long combinational paths and improve timing.
- Use `assert`/`report` for simulation-time validation.
- Organize code into entities/modules with clear port interfaces.
- Use clock-domain crossing (CDC) synchronization for跨时钟域 signals.

## Common Risks

- Incomplete sensitivity lists causing simulation-synthesis mismatch.
- Latch inference from incomplete `case` or `if` statements.
- Metastability from un-synchronized跨时钟域 signals.
- Timing closure issues from deep combinational logic.
- Simulation vs synthesis behavioral differences from non-synthesizable constructs.
