
import fi.helsinki.cs.tmc.edutestutils.Points;
import org.junit.Test;
import static org.junit.Assert.*;

public class TrivialTest {

//    private static final String PISTE = "1";

    @Test
    @Points("1.1")
    public void testF() {
        Trivial t = new Trivial();
        assertEquals(1, t.f());
    }

    @Test
    @Points("1.2")
    public void test2() {
        Trivial t = new Trivial();
        assertEquals(1, t.f());
    }
}
