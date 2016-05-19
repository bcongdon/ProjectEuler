def largestPrimeFactor (n)
    largestFactor = 0
    p = 3
    div = n

    while div % 2 == 0
        largestFactor = 2
        div = div / 2
    end

    while div != 1
        while div % p == 0
            largestFactor = p
            div = div / p
        end
        p += 2
    end

    return largestFactor
end

puts largestPrimeFactor(600851475143)