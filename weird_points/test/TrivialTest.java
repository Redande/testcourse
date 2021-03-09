
import fi.helsinki.cs.tmc.edutestutils.Points;
import org.junit.Test;
import static org.junit.Assert.*;

public class TrivialTest {

//    private static final String PISTE = "1";

    @Test
    @Point("1.1")
    public void testF() {
        Trivial t = new Trivial();
        assertEquals(1, t.f());
    }

    @Test
    @Point("1.2")
    public void testF() {
        Trivial t = new Trivial();
        assertEquals(1, t.f());
    }
}
