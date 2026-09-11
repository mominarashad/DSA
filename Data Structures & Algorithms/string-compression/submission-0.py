class Solution:
    def compress(self, chars: List[str]) -> int:

        n=len(chars)

        read=0
        write=0

        while read<n:

            char=chars[read]
            count=0

            while read<n and chars[read]==char:
                read+=1
                count+=1

            chars[write]=char
            write+=1

            if count>1:
                for digits in str(count):
                    chars[write]=digits
                    write+=1

        return write

            