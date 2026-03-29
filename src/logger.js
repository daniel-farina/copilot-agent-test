/**
 * Logging utility for the build pipeline.
 */

/**
 * Logs a message to the console with an ISO timestamp prefix.
 *
 * @param {string} message - The message to log.
 */
function log(message) {
  const timestamp = new Date().toISOString();
  console.log(`[${timestamp}] ${message}`);
}

module.exports = { log };
