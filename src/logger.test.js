const { log } = require('./logger');

describe('log', () => {
  let consoleSpy;

  beforeEach(() => {
    consoleSpy = jest.spyOn(console, 'log').mockImplementation(() => {});
  });

  afterEach(() => {
    consoleSpy.mockRestore();
  });

  test('outputs the provided message', () => {
    log('hello world');
    expect(consoleSpy).toHaveBeenCalledTimes(1);
    const output = consoleSpy.mock.calls[0][0];
    expect(output).toContain('hello world');
  });

  test('prefixes the message with an ISO timestamp', () => {
    const before = new Date();
    log('timestamp test');
    const after = new Date();

    const output = consoleSpy.mock.calls[0][0];
    // Extract the timestamp from the output "[<ts>] <msg>"
    const match = output.match(/^\[(.+?)\] /);
    expect(match).not.toBeNull();

    const ts = new Date(match[1]);
    expect(ts.getTime()).toBeGreaterThanOrEqual(before.getTime());
    expect(ts.getTime()).toBeLessThanOrEqual(after.getTime());
  });

  test('formats output as "[<timestamp>] <message>"', () => {
    jest.useFakeTimers().setSystemTime(new Date('2024-01-15T10:00:00.000Z'));
    log('formatted message');
    jest.useRealTimers();

    expect(consoleSpy).toHaveBeenCalledWith(
      '[2024-01-15T10:00:00.000Z] formatted message'
    );
  });
});
