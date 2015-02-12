import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class text_processing
{
	@SuppressWarnings("resource")
	public static void main(String[] args) throws IOException
	{
		//LinkedList<String> output_list = new LinkedList<String>();
		
		String text; 
		BufferedReader br = new BufferedReader(new FileReader("/home/matthias/Workbench/SUTD/1_February/brute_force/brutus_items.csv"));

		while ((text = br.readLine()) != null) 
		{
			//container
			//LinkedList<String> output_container = new LinkedList<String>();
			
			//the main character
			Pattern pat_0 = Pattern.compile( "『(.*?)』" );
			Matcher mat_0 = pat_0.matcher( text );
			if( mat_0.find() )
			{
			    System.out.println( mat_0.group(1) );
			    //output_container.add( mat_0.group(1) );
			    
			}
			//the pin yin
			Pattern pat_1 = Pattern.compile("class=\"\"pinyin\"\">(.*?)<script>(?:(?!<script>).)*");
			Matcher mat_1 = pat_1.matcher( text );
			if( mat_1.find() )
			{
			    System.out.println( mat_1.group(1) );
			    //output_container.add( mat_1.group(1) );
			}
			//the ubiquitous radical 
			Pattern pat_2 = Pattern.compile( "<span class=\"\"b\"\">部首：</span>" ); 
			Matcher mat_2 = pat_2.matcher( text );
			if( mat_2.find() )
			{
			    Pattern pat_3 = Pattern.compile("<span class=\"\"b\"\">部首：</span>(.*?)<span class=\"\"b\"\">");
			    Matcher mat_3 = pat_3.matcher( text );
			    if( mat_3.find() )
				{
			    	System.out.println("部首：" + mat_3.group(1) );
			    	//output_container.add( mat_3.group(1) );
				}
				//stroke count
				Pattern pat_4 = Pattern.compile(mat_3.group(1) + "<span class=\"\"b\"\">部首笔画：</span>(.*?)<span class=\"\"b\"\">");
				Matcher mat_4 = pat_4.matcher( text );
			    if( mat_4.find() )
				{
			    	System.out.println("笔画：" + mat_4.group(1) );
			    	//output_container.add( mat_4.group(1) );
				}

			}
			else
			{
				//simple rad
				Pattern pat_5 = Pattern.compile("简体部首：</span>(.*?)<span class=\"\"b\"\">");
			    Matcher mat_5 = pat_5.matcher( text );
			    if( mat_5.find() )
				{
			    	System.out.println("简体部首：" + mat_5.group(1) );
			    	//output_container.add( mat_5.group(1) );
				
			    	//stroke count
			    	Pattern pat_6 = Pattern.compile(mat_5.group(1) + "<span class=\"\"b\"\">部首笔画：</span>(.*?)<span class=\"\"b\"\">");
			    	Matcher mat_6 = pat_6.matcher( text );
			    	if( mat_6.find() )
			    	{
			    		System.out.println("简体笔画：" + mat_6.group(1) );
			    		//output_container.add( mat_6.group(1) );
			    	}
				}
			    
			    //trad rad
				Pattern pat_7 = Pattern.compile("繁体部首：</span>(.*?)<span class=\"\"b\"\">");
			    Matcher mat_7 = pat_7.matcher( text );
			    if( mat_7.find() )
				{
			    	System.out.println("繁体部首：" + mat_7.group(1) );
			    	//output_container.add( mat_7.group(1) );
				
			    	//stroke count
			    	Pattern pat_8 = Pattern.compile(mat_7.group(1) + "<span class=\"\"b\"\">部首笔画：</span>(.*?)<span class=\"\"b\"\">");
			    	Matcher mat_8 = pat_8.matcher( text );
			    	if( mat_8.find() )
			    	{
			    		System.out.println("繁体笔画：" + mat_8.group(1) );
			    		//output_container.add( mat_8.group(1) );
			    	}
				}
			    

			}
			
			//the decomposition
			Pattern pat_9 = Pattern.compile("#################,\" ]：(.*?)\\(");
			Matcher mat_9 = pat_9.matcher( text );
			if( mat_9.find() )
			{
			    System.out.println("首尾分解: " + mat_9.group(1) );
			    //output_container.add( mat_9.group(1) );
			}
			
			
			
		}
		
		
	}
}


    // #######################," ]：占乂(zhancha)
    // ","<table width=""620"" border=""0"" cellpadding=""0"" cellspacing=""0"">
    // <tr bgcolor=""#FFFFFF"">
    // <td width=""100""><div id=""zibg""><p class=""U5365""></p></div></td>
    // <td width=""510"" style=""padding-left:10px"">
    // <p class=""text15"">
    // 『卥』 <br>
    // <span class=""b"">拼音：</span><span class=""pinyin"">xī<script>Setduyin('Duyin/xi1')</script></span>　<span class=""b"">注音：</span><span class=""pinyin"">ㄒㄧ<script>Setduyin('Duyin/xi1')</script></span><br>
    // <span class=""b"">简体部首：</span>丨　<span class=""b"">部首笔画：</span>1　<span class=""b"">总笔画：</span>8<br><span class=""b"">繁体部首：</span>卜　<span class=""b"">部首笔画：</span>2　<span class=""b"">总笔画：</span>8<br><span class=""b"">康熙字典笔画</span>( 卥:8； )
    // </p></td>
    // </tr>
    // </table>"










