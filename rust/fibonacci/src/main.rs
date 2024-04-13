use anyhow::{anyhow, bail};

fn main() -> anyhow::Result<()> {
    let mut args = std::env::args();
    if args.len() != 2 {
        bail!("expected one argument")
    }
    let _ = args.next(); // 最初の引数はコマンド名のためスキップ
    let n = args
        .next()
        .unwrap()
        .parse::<u32>()
        .map_err(|e| anyhow!(e))?;

    // フィボナッチ数を求める
    let started = std::time::SystemTime::now();
    let value = fibonacci(n);
    let elapsed = started.elapsed().unwrap();
    let elapsed = elapsed.as_secs_f32();
    println!("fibonacci value: {value} ({elapsed:.3} seconds)");

    Ok(())
}

fn fibonacci(n: u32) -> u32 {
    match n {
        0 => 0,
        1 => 1,
        _ => fibonacci(n - 2) + fibonacci(n - 1),
    }
}
