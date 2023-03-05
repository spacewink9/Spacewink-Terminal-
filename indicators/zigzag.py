import numpy as np

def zigzag(data, deviation):
    """Calculate zigzag indicator values for the given data and deviation"""
    # Calculate differences between prices
    diffs = np.diff(data)
    # Initialize variables
    high = data[0]
    low = data[0]
    last_high = 0
    last_low = 0
    # Initialize zigzag array with NaNs
    zigzag = np.empty(len(data))
    zigzag.fill(np.nan)
    # Iterate over price differences and identify swing highs and lows
    for i in range(1, len(diffs)):
        # Update high and low values
        if diffs[i-1] > 0:
            high = data[i]
        elif diffs[i-1] < 0:
            low = data[i]
        # Check if a new swing high or low has been identified
        if high - low >= deviation:
            if diffs[i-1] < 0:
                last_high = high
                zigzag[i] = low
            elif diffs[i-1] > 0:
                last_low = low
                zigzag[i] = high
    # Set first and last values of zigzag to the first and last non-NaN values
    first_non_nan = np.where(np.logical_not(np.isnan(zigzag)))[0][0]
    last_non_nan = np.where(np.logical_not(np.isnan(zigzag)))[0][-1]
    zigzag[0:first_non_nan] = zigzag[first_non_nan]
    zigzag[last_non_nan+1:] = zigzag[last_non_nan]
    # Return zigzag array
    return zigzag
