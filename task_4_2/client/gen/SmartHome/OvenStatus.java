//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//
// Ice version 3.7.3
//
// <auto-generated>
//
// Generated from file `SmartHome.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

package SmartHome;

public class OvenStatus implements java.lang.Cloneable,
                                   java.io.Serializable
{
    public int heat;

    public int humidity;

    public OvenStatus()
    {
    }

    public OvenStatus(int heat, int humidity)
    {
        this.heat = heat;
        this.humidity = humidity;
    }

    public boolean equals(java.lang.Object rhs)
    {
        if(this == rhs)
        {
            return true;
        }
        OvenStatus r = null;
        if(rhs instanceof OvenStatus)
        {
            r = (OvenStatus)rhs;
        }

        if(r != null)
        {
            if(this.heat != r.heat)
            {
                return false;
            }
            if(this.humidity != r.humidity)
            {
                return false;
            }

            return true;
        }

        return false;
    }

    public int hashCode()
    {
        int h_ = 5381;
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, "::SmartHome::OvenStatus");
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, heat);
        h_ = com.zeroc.IceInternal.HashUtil.hashAdd(h_, humidity);
        return h_;
    }

    public OvenStatus clone()
    {
        OvenStatus c = null;
        try
        {
            c = (OvenStatus)super.clone();
        }
        catch(CloneNotSupportedException ex)
        {
            assert false; // impossible
        }
        return c;
    }

    public void ice_writeMembers(com.zeroc.Ice.OutputStream ostr)
    {
        ostr.writeInt(this.heat);
        ostr.writeInt(this.humidity);
    }

    public void ice_readMembers(com.zeroc.Ice.InputStream istr)
    {
        this.heat = istr.readInt();
        this.humidity = istr.readInt();
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, OvenStatus v)
    {
        if(v == null)
        {
            _nullMarshalValue.ice_writeMembers(ostr);
        }
        else
        {
            v.ice_writeMembers(ostr);
        }
    }

    static public OvenStatus ice_read(com.zeroc.Ice.InputStream istr)
    {
        OvenStatus v = new OvenStatus();
        v.ice_readMembers(istr);
        return v;
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, java.util.Optional<OvenStatus> v)
    {
        if(v != null && v.isPresent())
        {
            ice_write(ostr, tag, v.get());
        }
    }

    static public void ice_write(com.zeroc.Ice.OutputStream ostr, int tag, OvenStatus v)
    {
        if(ostr.writeOptional(tag, com.zeroc.Ice.OptionalFormat.VSize))
        {
            ostr.writeSize(8);
            ice_write(ostr, v);
        }
    }

    static public java.util.Optional<OvenStatus> ice_read(com.zeroc.Ice.InputStream istr, int tag)
    {
        if(istr.readOptional(tag, com.zeroc.Ice.OptionalFormat.VSize))
        {
            istr.skipSize();
            return java.util.Optional.of(OvenStatus.ice_read(istr));
        }
        else
        {
            return java.util.Optional.empty();
        }
    }

    private static final OvenStatus _nullMarshalValue = new OvenStatus();

    /** @hidden */
    public static final long serialVersionUID = -1372949094L;
}