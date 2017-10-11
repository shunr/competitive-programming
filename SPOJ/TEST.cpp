#include &lt;stdio.h&gt;
 
int main() {
	int x = 0;
	while(x != 42) {
		scanf("%i", &x);
		if (x != 42) printf("%i\n", x);
	}
}