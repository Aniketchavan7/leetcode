class MedianFinder {
    private final PriorityQueue<Integer> small = new PriorityQueue<>(Collections.reverseOrder()); // Max-heap
    private final PriorityQueue<Integer> large = new PriorityQueue<>(); // Min-heap

    public MedianFinder() {}

    public void addNum(int num) {
        small.add(num);
        large.add(small.poll()); // Balance values

        // Maintain size invariant: small >= large
        if (small.size() < large.size()) {
            small.add(large.poll());
        }
    }

    public double findMedian() {
        if (small.size() > large.size()) {
            return small.peek();
        }
        return (small.peek() + large.peek()) / 2.0;
    }
}
